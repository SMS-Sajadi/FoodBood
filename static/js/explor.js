document.getElementById('rest').addEventListener('click', ()=>{
    document.getElementById('rest').className = "choice_dish";
    document.getElementById('dish').className  = "choice_resturant";
    document.getElementById('foods').className = "offDive";
    document.getElementById('resturant_list').className = "onDive";
})

document.getElementById('dish').addEventListener('click', ()=>{
    document.getElementById('dish').className = "choice_dish";
    document.getElementById('rest').className  = "choice_resturant";
    document.getElementById('foods').className = "onDive";
    document.getElementById('resturant_list').classList = "offDive";

})

