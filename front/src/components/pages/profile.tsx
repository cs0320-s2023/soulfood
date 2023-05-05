import * as React from "react";
import Box from "@mui/material/Box";
import { Button, Typography } from "@mui/material";
import Tab from "@mui/material/Tab";
import TabContext from "@mui/lab/TabContext";
import TabList from "@mui/lab/TabList";
import TabPanel from "@mui/lab/TabPanel";
import { useUser } from "../dashboard";
import { doc, getDoc } from "firebase/firestore";
import { db } from "../../firebase/firebaseConfig";
import { ContentCardData } from "../Card";
import Grid from "@mui/material/Grid";
import ContentCard from "../Card";

export default function Profile() {
  const [value, setValue] = React.useState("posted");
  const [collected, setCollected] = React.useState<Array<ContentCardData>>([]);
  const [liked, setLiked] = React.useState<Array<ContentCardData>>([]);
  const [posted, setPosted] = React.useState<Array<ContentCardData>>([]);

  let { currentUser } = useUser();

  React.useEffect(() => {
    alert('called');
    /**
     * Returns post data from firestore given a list of PIDs
     */
    async function fetchPostData(
      pids: Array<string>,
      updateState: (posts: Array<ContentCardData>) => void
    ) {
      let collectedPosts: Array<ContentCardData> = [];
      for (let i = 0; i < pids.length; i++) {
        const docRef = doc(db, "posts", pids[i].toString());
        const docSnap = await getDoc(docRef);
        const data = docSnap.data();
        if (data !== undefined) {
          collectedPosts.push({
            pid: data["pid"],
            liked_by: data["liked_by"],
            collected_by: data["collected_by"],
            posted_by: data["posted_by"],
            labels: data["labels"],
            title: data["title"],
            paragraph: data["paragraph"],
            photo: data["photo"],
          });
        }
      }
      updateState(collectedPosts);
    }
    console.log(currentUser?.liked);
    if (currentUser !== undefined && currentUser !== null) {
      fetchPostData(currentUser.collected, setCollected);
      fetchPostData(currentUser.posted, setPosted);
      fetchPostData(currentUser.liked, setLiked);
    }
  }, [currentUser]);

  const handleChange = (event: React.SyntheticEvent, newValue: string) => {
    setValue(newValue);
  };

  return (
    <Box sx={{ flexGrow: 1, alignItems: "end", justifyContent: "center" }}>
      <Typography variant="h4" sx={{ fontWeight: "bold", mb: 2 }}>
        {currentUser !== null && currentUser.id}
      </Typography>
      <TabContext value={value}>
        <Box sx={{ borderBottom: 1, borderColor: "divider" }}>
          <TabList onChange={handleChange}>
            <Tab label="posted" value="posted" />
            <Tab label="collected" value="collected" />
            <Tab label="liked" value="liked" />
          </TabList>
        </Box>
        <TabPanel value="posted">
          <Grid container spacing={2}>
            {posted.map((data) => {
              return (
                <Grid item xs={4} key={data.pid}>
                  <ContentCard data={data} />
                </Grid>
              );
            })}
          </Grid>
        </TabPanel>
        <TabPanel value="collected">
          <Grid container spacing={2}>
            {collected.map((data) => {
              return (
                <Grid item xs={4} key={data.pid}>
                  <ContentCard data={data} />
                </Grid>
              );
            })}
          </Grid>
        </TabPanel>
        <TabPanel value="liked">
          <Grid container spacing={2}>
            {liked.map((data) => {
              return (
                <Grid item xs={4} key={data.pid}>
                  <ContentCard data={data} />
                </Grid>
              );
            })}
          </Grid>
        </TabPanel>
      </TabContext>
    </Box>
  );
}
