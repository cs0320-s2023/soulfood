import * as React from "react";
import { styled } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import MuiDrawer from "@mui/material/Drawer";
import Box from "@mui/material/Box";
import MuiAppBar, { AppBarProps as MuiAppBarProps } from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import List from "@mui/material/List";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import Container from "@mui/material/Container";
import MenuIcon from "@mui/icons-material/Menu";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import HomeIcon from "@mui/icons-material/Home";
import SearchIcon from "@mui/icons-material/Search";
import ExploreIcon from "@mui/icons-material/Explore";
import Person2Icon from "@mui/icons-material/Person2";
import LogoutIcon from "@mui/icons-material/Logout";
import CreateIcon from '@mui/icons-material/Create';

import { auth } from "../firebase/firebaseConfig";
import { signOut, onAuthStateChanged } from "@firebase/auth";

import { Outlet, Link, useNavigate, redirect, useOutletContext } from "react-router-dom";
import { ListItemButton, ListItemIcon, ListItemText } from "@mui/material";
import { fontWeight } from "@mui/system";

/** frontend for dashboard (first page user is taken to when accessing page) */

// drawer for opening and closing left bar
const drawerWidth: number = 240;

interface AppBarProps extends MuiAppBarProps {
  open?: boolean;
}

interface User {
  uid: string,
  id: string,
  bio: string,
  following: Array<string>,
  followed_by: Array<string>,
  liked: Array<string>,
  collected: Array<string>,
  posted: Array<string>
}

type ContextType = { currentUser: User | null, setCurrentUser: (user: User) => void }

// app bar styling (left side)
const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== "open",
})<AppBarProps>(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(["width", "margin"], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(["width", "margin"], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

// drawer styling (opening and closing app bar)
const Drawer = styled(MuiDrawer, {
  shouldForwardProp: (prop) => prop !== "open",
})(({ theme, open }) => ({
  "& .MuiDrawer-paper": {
    position: "relative",
    whiteSpace: "nowrap",
    width: drawerWidth,
    transition: theme.transitions.create("width", {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
    boxSizing: "border-box",
    ...(!open && {
      overflowX: "hidden",
      transition: theme.transitions.create("width", {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.leavingScreen,
      }),
      width: theme.spacing(7),
      [theme.breakpoints.up("sm")]: {
        width: theme.spacing(9),
      },
    }),
  },
}));

// interface DashboardProps {
//   component: React.ReactElement,
// }

export default function Dashboard() {
  
  const [currentUser, setCurrentUser] = React.useState<User | null>(null);
  const [open, setOpen] = React.useState(true);

  // changes data displayed if user is changed
  React.useEffect(() => {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        //`http://127.0.0.1:5000/search/user/${uid}`
        fetch("http://127.0.0.1:5000/search/user/1")
          .then((res) => res.json())
          .then((data) => {
            // sets user data to the data obtained from calling backend server
            setCurrentUser({
              uid: data['uid'],
              id: data['id'],
              followed_by: data['followed_by'],
              following: data['following'],
              collected: data['collected'],
              bio: data['bio'],
              liked: data['liked'],
              posted: data['posted']
            });
          })
      } else {
        setCurrentUser(null)
      }
    });
  }, []);

  const navigate = useNavigate();

  const toggleDrawer = () => {
    setOpen(!open);
  };

  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      {/* app bar element */}
      <AppBar elevation={0} position="absolute" open={open} color="secondary">
        <Toolbar
          sx={{
            pr: "24px", // keep right padding when drawer closed
          }}
        >
          {/* button to open and close the apps on the left */}
          <IconButton
            edge="start"
            color="inherit"
            aria-label="open drawer"
            onClick={toggleDrawer}
            sx={{
              marginRight: "36px",
              ...(open && { display: "none" }),
            }}
          >
            {/* menu icon */}
            <MenuIcon />
          </IconButton>
          {/* SoulFood */}
          <Typography variant="h6" sx={{ flexGrow: 1 }}>SoulFood</Typography>
          <IconButton onClick={() => {
            signOut(auth).then(() => {
              navigate('/login')
            }).catch((error) => {
              alert(error);
            });
          }}>
            {/* logout icon */}
            <LogoutIcon />
          </IconButton>
          <Typography>
            {auth.currentUser?.email}
          </Typography>
        </Toolbar>
      </AppBar>
      <Drawer variant="permanent" open={open}>
        <Toolbar
          sx={{
            display: "flex",
            alignItems: "center",
            justifyContent: "flex-end",
            px: [1],
          }}
        >
          <IconButton onClick={toggleDrawer}>
            <ChevronLeftIcon />
          </IconButton>
        </Toolbar>
        <Divider />
        {/* contains different pages of frontend site */}
        <List component="nav">
          <ListItemButton role="home" onClick={() => navigate("/home")}>
            <ListItemIcon>
              <HomeIcon />
            </ListItemIcon>
            <ListItemText primary="Home" />
          </ListItemButton>
          <ListItemButton role="explore" onClick={() => navigate("/explore")}>
            <ListItemIcon>
              <ExploreIcon />
            </ListItemIcon>
            <ListItemText primary="Explore" />
          </ListItemButton>
          <ListItemButton role="search" onClick={() => navigate("/search")}>
            <ListItemIcon>
              <SearchIcon />
            </ListItemIcon>
            <ListItemText primary="Search" />
          </ListItemButton>
          <ListItemButton role="profile" onClick={() => navigate("/profile")}>
            <ListItemIcon>
              <Person2Icon />
            </ListItemIcon>
            <ListItemText primary="Profile" />
          </ListItemButton>
          <ListItemButton role="create" onClick={() => navigate("/create")}>
            <ListItemIcon>
              <CreateIcon />
            </ListItemIcon>
            <ListItemText primary="Create" />
          </ListItemButton>
        </List>
      </Drawer>
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          height: "100vh",
          overflow: "auto",
        }}
      >
        <Toolbar />
        <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
          <Outlet context={{ currentUser, setCurrentUser }}/>
        </Container>
      </Box>
    </Box>
  );
}

export function useUser() {
  return useOutletContext<ContextType>();
}