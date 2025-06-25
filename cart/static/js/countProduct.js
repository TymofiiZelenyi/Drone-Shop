function countProduct(button) {
    cookies = document.cookie.split('=')[1] // ['list_products', '|1||1||2||3|']
    listCookies = cookies.split('|') // ['', '1', '', '1', '', '2', '', '3']
    let count = 0
    for (let id of listCookies) {
       if (id == button.id){
            count += 1
       }
    }   
}