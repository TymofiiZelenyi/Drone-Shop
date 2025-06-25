const listButtonsPlus = document.querySelectorAll(".plus")

for (let button of listButtonsPlus){
    button.addEventListener(
        type = 'click',
        listener = function (event){
            cookies = document.cookie.split('=')[1]
            document.cookie = `list_products = ${cookies}|${button.id}|; path = /`
        }
    )
}