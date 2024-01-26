document.getElementById('pop').addEventListener('click', ()=>{
    document.getElementById('pop').className = "on_choice";
    document.getElementById('burger').className  = "choice";
    document.getElementByClassName('fries').className  = "choice";
    document.getElementByClassName('drinks').className  = "choice";
    document.getElementByClassName('pop_list').className = "onDive";
    document.getElementByClassName('burger_list').className = "offDive";
    document.getElementByClassName('fries_list').className = "offDive";
    document.getElementByClassName('drinks_list').className = "offDive";
})


document.getElementById('burger').addEventListener('click', ()=>{
    document.getElemenByClassName('burger').className = "on_choice";
    document.getElementByClassName('pop').className  = "choice";
    document.getElementByClassName('fries').className  = "choice";
    document.getElementByClassName('drinks').className  = "choice";
    document.getElementsByClassName('burger_list').className = "onDive";
    document.getElementByClassName('pop_list').className = "offDive";
    document.getElementByClassName('fries_list').className = "offDive";
    document.getElementByClassName('drinks_list').className = "offDive";
})
