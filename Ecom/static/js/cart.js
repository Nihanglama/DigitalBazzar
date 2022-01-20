var btn=document.getElementsByClassName("addtocart")
for(var i=0 ; i<btn.length;i++){
    btn[i].addEventListener('click',function(){
        var productId=this.dataset.product
        var action=this.dataset.action
        
        if(user==='AnonymousUser'){
            alert("Please Login to add item in cart")

        }
        else{
            updateCart(productId,action)
        }

    })

    
}

function updateCart(productId,  action){
    var url = '/updatecart/'
    fetch(url,{
        method:'POST', 
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken
        },
        body:JSON.stringify({'productId':productId,'action': action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data)=>{
        location.reload()
    })


}