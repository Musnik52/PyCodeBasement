$(document).ready(function()
{
    $('#btn1').on('click', () => {

        var $users =  $("#users"); //cache

        $.ajax({url:"https://jsonplaceholder.typicode.com/users"}).then(
                function(_users) // after-promise succeed
                {
                    console.log(_users);

                   $.each(_users,  (i, user) => {
                                $users.append(
                                    `<tr><td>${user.id}</td>
                                         <td>${user.name}</td>
                                         <td>${user.username}</td>
                                         <td>${user.email}</td></tr>`)
                    })
                }
                ,function(err)   // after-promise failed
                { 
                    console.log(err);}		
                );
    });
});