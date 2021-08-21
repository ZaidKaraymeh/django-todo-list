var editor = document.getElementById("editor");
let csrftoken = getCookie("csrftoken");

editor.addEventListener("input", function () {
  text = document.getElementById("contentedit").value = editor.innerHTML;
    console.log(text)
  fetch("change_name/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(data),
    credentials: "same-origin",
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success: ", data);
    })
    .catch((error) => {
      console.error("My Error: ", error);
    });
});
