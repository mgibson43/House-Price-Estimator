(() => {
 'use strict'

  // Initialize city and state URLS
  let stateUrl = '/state-json/'

  // Get state and city dropdown menus
  const stateBox = document.getElementById('state')
  const cityBox = document.getElementById('city')
 
  // Fetch state data from database and set each state dropdown option
  fetch(stateUrl)
    .then(response => response.json())
    .then(data => {
      const stateData = data.data

      stateData.map(item=>{
        const option = document.createElement('option')
        option.textContent = item.id
        option.setAttribute('class', 'item')
        option.setAttribute('value', item.id)
        stateBox.appendChild(option)
      })
    })
    .catch(error => console.error('Error:', error))

  // Update city dropdown menu based on selected state
  function updateCity(e) {
    cityBox.innerHTML = ''
    setCityDefault()
    const selectedState = e.target.value

    // Use get response to retrieve only cities that are located within the selected state
    if (selectedState != '') {
      fetch(`models-json/${selectedState}/`)
      .then(response => response.json())
      .then(data => {
        const cityData = data.data

        // Set city dropdown menu options
        cityData.map(item=>{
          const option = document.createElement('option')
          option.textContent = item.id
          option.setAttribute('class', 'item')
          option.setAttribute('value', item.id)
          cityBox.appendChild(option)
        })
      })
      .catch(error => console.error('Error:', error))
    }  
  }

  // Set the city and state dropdown menus to a default configuration
  function setCityDefault() {
    const cityDefault = document.createElement('option')
    cityDefault.textContent = '----------'
    cityDefault.setAttribute('class', 'item')
    cityDefault.setAttribute('value', '')
    cityBox.appendChild(cityDefault)
  }

  function setStateDefault() {
    const stateDefault = document.createElement('option')
    stateDefault.textContent = '----------'
    stateDefault.setAttribute('class', 'item')
    stateDefault.setAttribute('value', '')
    stateBox.appendChild(stateDefault)
  }

  // Listen for changes in the state dropdown menu and update city dropdown menu accordingly
  stateBox.addEventListener("change", updateCity)

  setStateDefault()
  setCityDefault()
})()