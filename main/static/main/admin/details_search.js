// search.js


document.addEventListener('DOMContentLoaded', function () {


    const alert = document.getElementById("js_mes");
    const perfumeSearchInput = document.querySelector('#perfume-search-input-mu');
    const perfumeSuggestions = document.querySelector('#perfume-suggestions-mu');
    const searchForm = document.querySelector('#search-form-mu');
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    const clientId = document.getElementById("hidden-id").value;


    const handleAlerts = (type, mes) => {
        alert.innerHTML = `<div class="alert alert-${type}" role="alert">
                                ${mes}
                            </div>`
    }




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
                    
                        const p_val = perfume.name + ' от ' + perfume.brand + ' | ' + perfume.ml + 'ml' + ' - ' + perfume.price + 'TMT';
                    
                        suggestion.textContent = p_val;
                    
                        // Adding inline styles to the suggestion element for a border
                        suggestion.style.border = '1px solid #1b00ff'; // Light grey border
                        suggestion.style.padding = '5px'; // Adding some padding for better appearance
                        suggestion.style.margin = '3px 0'; // Adding some margin between suggestions
                        suggestion.style.color = 'white'; // Adding some margin between suggestions
                        suggestion.style.backgroundColor = '#1b00ff'; // Adding some margin between suggestions
                        suggestion.style.borderRadius = '5px'; // Adding some border radius
                    
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
        perfumeId = perfumeSearchInput.dataset.perfumeId;

        fd.append('csrfmiddlewaretoken', csrf[0].value)
        fd.append('parfume', perfumeId)
        fd.append('client', clientId)



        // const userId = userSearchInput.dataset.userId;
        // const perfumeId = perfumeSearchInput.dataset.perfumeId;
        if (perfumeId) {
            $.ajax({
                url: '/add_purchase_details/',
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
                        perfumeId = ''
                        perfumeSearchInput.value = ""
                        location.reload();
                    }, 1)

                },
                error: function (xhr, status, error) {
                    console.error('Error adding purchase:', error);
                    // Handle error response
                    handleAlerts('danger', 'Ошибка..')
                    setTimeout(()=>{
                        alert.innerHTML = ""
                       
                        userSearchInput.value = ""
                        perfumeSearchInput.value = ""
                        
                    }, 2000)
                },
                cache: false,
                contentType: false,
                processData: false,
            });
        }
    });
});



