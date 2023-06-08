import { initializeApp } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "https://www.gstatic.com/firebasejs/9.4.0/firebase-auth.js";

const firebaseConfig = {
    // Firebase configuration details
};

const app = initializeApp(firebaseConfig);
const auth = getAuth();

document.addEventListener("DOMContentLoaded", function () {
    let btnLogin = document.getElementById("login");
    let btnSignUp = document.getElementById("signup");

    let signIn = document.querySelector(".signin");
    let signUp = document.querySelector(".signup");

    btnLogin.onclick = function () {
        signIn.classList.add("active");
        signUp.classList.add("inActive");
    };

    btnSignUp.onclick = function () {
        signIn.classList.remove("active");
        signUp.classList.remove("inActive");
    };

    document.querySelector(".forget-password a").addEventListener("click", () => {
        const email = document.getElementById("emailLogin").value;

        auth.sendPasswordResetEmail(email)
            .then(() => {
                alert(`Password reset email sent to ${email}!`);
            })
            .catch((error) => {
                alert(error.message);
            });
    });
});


// let btnLogin = document.getElementById("login");
// let btnSignUp = document.getElementById("signup");

// let signIn = document.querySelector(".signin");
// let signUp = document.querySelector(".signup");

// btnLogin.onclick = function(){
//     signIn.classList.add("active");
//     signUp.classList.add("inActive");
// }

// btnSignUp.onclick = function(){
//    signIn.classList.remove("active");
//    signUp.classList.remove("inActive");
// }

