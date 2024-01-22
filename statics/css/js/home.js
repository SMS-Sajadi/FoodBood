document.getElementById('my_btn').addEventListener('click', function() {

  var myButton = document.getElementById('my_btn');

     
      if (myButton.classList.contains('left-menu')) {
        
        myButton.classList.remove('left-menu');
        myButton.classList.add('purpleBackground');
      } else {
     
        myButton.classList.remove('purpleBackground');
        myButton.classList.add('left-menu');
      }
  });
  
  document.getElementById('my_btn2').addEventListener('click', function() {

    var myButton = document.getElementById('my_btn2');
  
       
        if (myButton.classList.contains('left-menu')) {
          
          myButton.classList.remove('left-menu');
          myButton.classList.add('purpleBackground');
        } else {
       
          myButton.classList.remove('purpleBackground');
          myButton.classList.add('left-menu');
        }
    });
    document.getElementById('my_btn3').addEventListener('click', function() {

      var myButton = document.getElementById('my_btn3');
    
         
          if (myButton.classList.contains('left-menu')) {
            
            myButton.classList.remove('left-menu');
            myButton.classList.add('purpleBackground');
          } else {
         
            myButton.classList.remove('purpleBackground');
            myButton.classList.add('left-menu');
          }
      });
      document.getElementById('my_btn4').addEventListener('click', function() {

        var myButton = document.getElementById('my_btn4');
      
           
            if (myButton.classList.contains('left-menu')) {
              
              myButton.classList.remove('left-menu');
              myButton.classList.add('purpleBackground');
            } else {
           
              myButton.classList.remove('purpleBackground');
              myButton.classList.add('left-menu');
            }
        });
        document.getElementById('my_btn5').addEventListener('click', function() {

          var myButton = document.getElementById('my_btn5');
        
             
              if (myButton.classList.contains('left-menu')) {
                
                myButton.classList.remove('left-menu');
                myButton.classList.add('purpleBackground');
              } else {
             
                myButton.classList.remove('purpleBackground');
                myButton.classList.add('left-menu');
              }
          });          
          
          function goTo_orders()
           {
          
            window.location.href = 'orders.html';
          }