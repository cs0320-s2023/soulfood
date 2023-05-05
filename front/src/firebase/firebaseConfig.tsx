import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyA5gbCx89_pWx2w6grsByqPgIknTRXocqE",
  authDomain: "soulfood-59503.firebaseapp.com",
  projectId: "soulfood-59503",
  storageBucket: "soulfood-59503.appspot.com",
  messagingSenderId: "713335695405",
  appId: "1:713335695405:web:5181eedf54fcdf008730a4",
  measurementId: "G-T2RZLPVEBX"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const auth = getAuth(app);
const db = getFirestore(app);

export { app, analytics, auth, db };
