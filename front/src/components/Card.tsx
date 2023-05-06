import * as React from "react";
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import CardActions from '@mui/material/CardActions';
import FavoriteIcon from '@mui/icons-material/Favorite';
import IconButton from '@mui/material/IconButton';
import { useUser } from "./dashboard";
import { doc, getDoc, updateDoc, arrayUnion, arrayRemove } from "firebase/firestore";
import { db } from "../firebase/firebaseConfig";

/**
 * frontend for each 'card' that is being displayed; these cards contain user, review, and post data
 */

export interface ContentCardData {
  pid: string,
  liked_by: Array<string>,
  collected_by: Array<string>,
  title: string,
  paragraph: string,
  labels: Array<string>,
  posted_by: string,
  photo: string
}

interface ContentCardProps {
  data: ContentCardData
}

export default function ContentCard(props: ContentCardProps) {

  const { currentUser, setCurrentUser } = useUser();

  const [liked, setLiked] = React.useState(isLiked());

  // handles when a user likes a post
  async function handleLike() {
    if (currentUser === undefined || currentUser === null) {
      return;
    }
    const userRef = doc(db, "profiles", currentUser.uid.toString());
    const postRef = doc(db, "posts", props.data.pid.toString());
    
    if (liked) {
      // removes user id who liked the post
      await updateDoc(userRef, {
        liked: arrayRemove(props.data.pid)
      });
      await updateDoc(postRef, {
        liked_by: arrayRemove(currentUser.uid)
      });
      const newLiked = currentUser.liked.filter(item => item !== props.data.pid)
      setCurrentUser({
        ...currentUser,
        liked: newLiked
      });
      setLiked(false);
    } else {
      // adds user id who liked the post
      await updateDoc(userRef, {
        liked: arrayUnion(props.data.pid)
      });
      await updateDoc(postRef, {
        liked_by: arrayUnion(currentUser.uid)
      });
      const newLiked = [...currentUser.liked, props.data.pid];
      setCurrentUser({
        ...currentUser,
        liked: newLiked
      });
      setLiked(true);
    }
  }

  // returns whether a post is liked by the current user
  function isLiked() {
    if (currentUser === undefined || currentUser === null) {
      return false;
    }
    console.log(props.data.pid)
    console.log(props.data.liked_by)
    return props.data.liked_by.includes(currentUser.uid);
  }

  return (
      <Card>
        <CardHeader
          title={props.data.title}
        />
        <CardMedia
          component="img"
          src={props.data.photo}
          height={250}
          alt={props.data.title}
        />
        <CardContent sx={{ height: 100, overflow: "hidden"}}>
          <Typography  variant="body2" color="text.secondary" sx={{ textOverflow: "ellipsis" }}>
            {props.data.paragraph}
          </Typography>
        </CardContent>
        <CardActions disableSpacing>
          <IconButton onClick={handleLike} color={liked ? 'error' : 'default'} aria-label="add to favorites">
            <FavoriteIcon />
          </IconButton>
        </CardActions>
      </Card>
  );
}