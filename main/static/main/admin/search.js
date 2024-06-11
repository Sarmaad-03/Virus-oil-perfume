// search.js


document.addEventListener('DOMContentLoaded', function () {


    const alert = document.getElementById("js_mes");
    const userSearchInput = document.querySelector('#user-search-input-mu');
    const perfumeSearchInput = document.querySelector('#perfume-search-input-mu');
    const userSuggestions = document.querySelector('#user-suggestions-mu');
    const perfumeSuggestions = document.querySelector('#perfume-suggestions-mu');
    const searchForm = document.querySelector('#search-form-mu');

    const csrf = document.getElementsByName('csrfmiddlewaretoken')

    const handleAlerts = (type, mes) => {
        alert.innerHTML = `<div class="alert alert-${type}" role="alert">
                                ${mes}
                            </div>`
    }



    userSearchInput.addEventListener('input', function (e) {
        const query = e.target.value.trim();
        if (query !== '') {
            $.ajax({
                url: '/get_items_user/',
                data: { 'query': query },
                dataType: 'json',
                success: function (data) {
                    userSuggestions.innerHTML = '';
                    data.forEach(user => {
                        const suggestion = document.createElement('div');
                        suggestion.textContent = user.username;
                        suggestion.textContent = user.surname;
                        suggestion.textContent = user.dob;
                        suggestion.textContent = user.purchases;

                        const s_val = user.username + ' ' + user.surname + ' | ' + user.dob + ' | ' + ' | покупки: ' + user.purchases

                        suggestion.textContent = s_val;

                        suggestion.dataset.userId = user.id; // Storing user ID as data attribute
                        suggestion.addEventListener('click', function () {
                            
                            userSearchInput.value = user.username + ' ' + user.surname + ' |год рождения: ' + user.dob;
                            userSearchInput.dataset.userId = user.id; // Storing user ID in input dataset
                            userSuggestions.innerHTML = '';
                        });
                        userSuggestions.appendChild(suggestion);
                    });
                }
            });
        } else {
            userSuggestions.innerHTML = '';
        }
    });

    perfumeSearchInput.addEventListener('input', function (e) {
        const query = e.target.value.trim();
        if (query !== '') {
            $.ajax({
                url: '/get_items_parfume/',
                data: { 'query': query },
                dataType: 'json',
                success: function (data) {
                    perfumeSuggestions.innerHTML = '';
                    data.forEach(perfume => {
                        const suggestion = document.createElement('div');
                        
                        const p_val = perfume.name + ' by ' + perfume.brand + ' | ' + perfume.ml + 'ml' +' - '+ perfume.price + 'TMT'
                        
                        suggestion.textContent = p_val;

                        suggestion.dataset.perfumeId = perfume.id; // Storing perfume ID as data attribute
                        suggestion.addEventListener('click', function () {
                            perfumeSearchInput.value = p_val;
                            perfumeSearchInput.dataset.perfumeId = perfume.id; // Storing perfume ID in input dataset
                            perfumeSuggestions.innerHTML = '';
                        });
                        perfumeSuggestions.appendChild(suggestion);
                    });
                }
            });
        } else {
            perfumeSuggestions.innerHTML = '';
        }
    });

    searchForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const fd = new FormData()
        const userId = userSearchInput.dataset.userId;
        const perfumeId = perfumeSearchInput.dataset.perfumeId;

        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('user', userId)
        fd.append('parfume', perfumeId)



        // const userId = userSearchInput.dataset.userId;
        // const perfumeId = perfumeSearchInput.dataset.perfumeId;
        if (userId && perfumeId) {
            $.ajax({
                url: '/add_purchase/',
                type: 'POST',
                headers: {
                    'X-CSRFToken': csrf
                },
                data: fd,
                
                success: function (response) {
                    console.log('Successfully added purchase:', response);
                    // Handle success response
                    handleAlerts('success', 'Успешно добавлено.')
                    setTimeout(()=>{
                        alert.innerHTML = ""
                       
                        userSearchInput.value = ""
                        perfumeSearchInput.value = ""
                        
                    }, 3000)
                },
                error: function (xhr, status, error) {
                    console.error('Error adding purchase:', error);
                    // Handle error response
                    handleAlerts('danger', 'Ошибка..')
                    setTimeout(()=>{
                        alert.innerHTML = ""
                       
                        userSearchInput.value = ""
                        perfumeSearchInput.value = ""
                        
                    }, 3000)
                },
                cache: false,
                contentType: false,
                processData: false,
            });
        }
    });
});



