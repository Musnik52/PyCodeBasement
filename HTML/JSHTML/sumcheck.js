console.log('loading index.js code...')
function btn_click() 
{
    // alert('clicked me')
    document.getElementById('result').innerHTML = 
      document.getElementById('fname_txt').value + ' ' +
      document.getElementById('lname_txt').value
}