import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDwgB9OVfzlDWjh6XWq1l_7t1K57meE4-o",
  authDomain: "soulfood-cf39a.firebaseapp.com",
  projectId: "soulfood-cf39a",
  storageBucket: "soulfood-cf39a.appspot.com",
  messagingSenderId: "112290426464",
  appId: "1:112290426464:web:51934874118e34797a1d05",
  measurementId: "G-MHKMTWH65E"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);
const db = getFirestore(app);

export { app, analytics, auth, db };


