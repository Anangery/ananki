let front = document.getElementById("front");
let back = document.getElementById("back");
let content = [];

document.addEventListener("keydown", function(e) {
    if (e.ctrlKey && e.key === "Enter"){
        submit()
        e.preventDefault();
    }
});

function submit(){
    content.push({
        key: front.value,
        value: back.value
    });
    console.log(content);
    front.value = null;
    back.value = null;
    front.focus();
}

function done() {
    console.log("done");
}