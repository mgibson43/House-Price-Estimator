let stateUrl = '/state-json/'
let cityUrl = '/city-json/'

const stateBox = document.getElementById('state')
const cityBox = document.getElementById('city')

setStateDefault()

setCityDefault()

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

stateBox.addEventListener("change", updateCity)

function updateCity(e) {
  cityBox.innerHTML = ''
  setCityDefault()
  const selectedState = e.target.value

  if (selectedState != '') {
    fetch(`models-json/${selectedState}/`)
    .then(response => response.json())
    .then(data => {
      const cityData = data.data

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