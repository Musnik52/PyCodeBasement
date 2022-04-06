console.log('loading index.js code...')
function btn_click() 
{
    // alert('clicked me')
    x = parseInt(document.getElementById('x_txt').value)
    y = parseInt(document.getElementById('y_txt').value)
    document.getElementById('result').innerHTML = 
       x + ' + ' + y + ' = ' + (x + y);
}