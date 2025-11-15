// The idea is to toggle between login and registration forms, show or hide the login popup, and close the popup.

const wrapper=document.queryselector(".wrapper");
const loginlink=document.queryselector(".loginlink");
const registerlink=document.queryselector(".registerlink");
const btn-popup=document.queryselector(".btn-login-popup");
const iconClose=document.queryselector(".icon-close");


registerlink.addEventlistener("click",()=>{
  wrapper.classlist.add("active");//The class active could be used in the CSS to display the registration form (by changing the visibility or layout).
})

loginlink.addEventlistener("click",()=>{
  wrapper.classlist.remove("active");//The code removes the class active from the wrapper.This likely switches back to the login form (removing the class might hide the registration form and show the login form).
})

btnpopup.addEventlistener("click",()=>{
  wrapper.classlist.add("active-popup");
})

iconClose.addEventlistener("click",()=>{
  wrapper.classlist.remove("active-popup");
})