let countHTML = document.getElementById("name")
let addBtn = document.getElementById("add-btn")
let clearBtn = document.getElementById("clear-btn")

let n = ""

const updateCountDom = (value) => {
    countHTML.innerHTML = value.toString()
}

addBtn.addEventListener("click", () => {
    n = "Preetham Kamishetty";
    updateCountDom(n)
})

clearBtn.addEventListener("click", () => {
    n = "";
    updateCountDom(n)
})