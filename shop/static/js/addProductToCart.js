const listButtons = document.querySelectorAll('.buy')

for (let button of listButtons){
    button.addEventListener(
        type = 'click',
        listener = function (event){
            listIdProducts = document.cookie.split('=')[1]
            if (document.cookie == '' || !listIdProducts){
                document.cookie = `list_products = |${button.id}|; path = /`
            }
            else{
                document.cookie = `list_products = ${listIdProducts}|${button.id}|; path = /`
            }
        }
    )
}

