/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


document.addEventListener("DOMContentLoaded",()=>{
    const themeSwitch = document.getElementById("themeSwitch");
    const themeLabel = document.querySelector(".form-check-label");

    themeSwitch.addEventListener("change",()=>{
        let newTheme = this.checked?"dark":"light";

        fetch("{% url 'set_theme' %}?theme=" + newTheme, { method: "GET" })
                .then(() => location.reload());
    })
})