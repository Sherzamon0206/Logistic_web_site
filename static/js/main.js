


function share_weight() {


    weight1 = document.getElementById(`weight`).value

    height = document.getElementById(`height`).value
    length = document.getElementById(`length`).value
    width = document.getElementById(`width`).value

    country = document.getElementById(`country_id1`).value
    if( weight1!="" && weight1<9.51){
                                                    if (weight1 <= 0.5) {
                                                        weight1 = 0.5;
                                                        console.log(weight1)
                                                    } else if (weight1 > 0.5 && weight1 <= 1) {
                                                        weight1 = 1;
                                                        console.log(weight1)
                                                    } else if (weight1 > 1 && weight1 <= 1.5) {
                                                        weight1 = 1.5;
                                                        console.log(weight1)
                                                    } else if (weight1 > 1.5 && weight1 <= 2) {
                                                        weight1 = 2;
                                                        console.log(weight1)
                                                    } else if (weight1 > 2 && weight1 <= 2.5) {
                                                        weight1 = 2.5;console.log(weight1)
                                                    } else if (weight1 > 2.5 && weight1 <= 3) {
                                                        weight1 = 3;console.log(weight1)
                                                    } else if (weight1 > 3 && weight1 <= 3.5) {
                                                        weight1 = 3.5;console.log(weight1)
                                                    } else if (weight1 > 3.5 && weight1 <= 4) {
                                                        weight1 = 4;console.log(weight1)
                                                    } else if (weight1 > 4 && weight1 <= 4.5) {
                                                        weight1 = 4.5;console.log(weight1)
                                                    } else if (weight1 > 4.5 && weight1 <= 5) {
                                                        weight1 = 5;console.log(weight1)
                                                    } else if (weight1 > 5 && weight1 <= 5.5) {
                                                        weight1 = 5.5;console.log(weight1)
                                                    } else if (weight1 > 5.5 && weight1 <= 6) {
                                                        weight1 = 6;console.log(weight1)
                                                    } else if (weight1 > 6 && weight1 <= 6.5) {
                                                        weight1 = 6.5;console.log(weight1)
                                                    } else if (weight1 > 6.5 && weight1 <= 7) {
                                                        weight1 = 7;console.log(weight1)
                                                    } else if (weight1 > 7 && weight1 <= 7.5) {
                                                        weight1 = 7.5;console.log(weight1)
                                                    } else if (weight1 > 7.5 && weight1 <= 8) {
                                                        weight1 = 8;console.log(weight1)
                                                    } else if (weight1 > 8 && weight1 <= 8.5) {
                                                        weight1 = 8.5;console.log(weight1)
                                                    } else if (weight1 > 8.5 && weight1 <= 9) {
                                                        weight1 = 9;console.log(weight1)
                                                    } else if (weight1 > 9 && weight1 <= 9.5) {
                                                        weight1 = 9.5;console.log(weight1)} }

    else  {  weight1 = Math.ceil(weight1); console.log(weight1)}
    if (height != "" && width != "" && length != "") {
        kg =(170 * height * width * length)/1000000;
        kg=Math.ceil(kg)
        document.getElementById("dimentional_label").innerHTML=kg

        console.log(kg)

        if(weight1>kg){
            document.getElementById("chargeable_label").innerHTML=weight1
            natija=weight1

        }
        else {
            document.getElementById("chargeable_label").innerHTML=kg
            natija=kg
        }
    }
    else {document.getElementById("chargeable_label").innerHTML=weight1
        natija=weight1

    }




        var url = `/calculator/`
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({

                'weight': natija,

            })
        })
            .then((response) => {
                response.json().then((data) => {
                    data = data['data']
                    console.log(data)
                    document.getElementById("umumiy_massa").innerHTML=natija
                })
            })
    }



    function weight_data() {
        country = document.getElementById(`country_id1`).value
        weight = document.getElementById(`umumiy_massa`).innerHTML

        var url = `/company/`
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'country': country,
                'weight': weight,
            })
        })
            .then((response) => {
                response.json().then((data) => {
                    data = data['data']

                    html=`
                    <section>
                            <div class="header_fixed">
                              <table>
                                  <thead>
                                      <tr>
                               
                                          <th>Logo</th>
                                          <th>Courier</th>
                                          <th>Service Type</th>
                                          <th>Transit Time</th>
                                          <th>Rate</th>
                                          <th>Submit</th>
                                      </tr>
                                  </thead>
                                   <tbody>`
                    for (var i = 0; i < data.length; i++) {
                                            html += `    
                                  
                                      <tr>
                                          
                                          <td><img src="${data[i].logo}" alt="Company logo" ></td>
                                          <td>${data[i].name}</td>
                                          <td>${data[i].type}</td>
                                          <td>${data[i].time}</td>
                                          <td>${data[i].price} $</td>
                                          <td><button onclick='d2("${data[i].name}", ${data[i].price})' >Submit</button>
                                          
                                      </tr>` }
                    html+=` </tbody>
                              </table>
                          </div>
                          </section>`





                    document.getElementById('3div').innerHTML = html

                })
            })
    }


    function sherzamon() {
        country = document.getElementById(`country_id1`).value
        weight = document.getElementById(`umumiy_massa`).innerHTML
        console.log(country)
        console.log(weight)
        if (country != "" && weight != "") {
            weight_data()
            document.getElementById("1div").hidden = !document.getElementById("1div").hidden;
            document.getElementById("3div").hidden = !document.getElementById("3div").hidden;


        } else {
            document.getElementById("text12").innerHTML = `<b style="color:red" >  Sizda qaysidir bo'lim to'ldirilmagan please</b>`
        }
    }






    function d2(name, price) {
        document.getElementById("3div").hidden = !document.getElementById("3div").hidden;
        document.getElementById("4div").hidden = !document.getElementById("4div").hidden;


        document.getElementById('4div').innerHTML = `  <div  class="wrapper">
            <div class="title">
              Registration Form
            </div>
            <div class="form">
              <div class="inputfield">
                <label>Name</label>
                <input id="name" type="text" class="input">
              </div>
           
              <div class="inputfield">
                <label>Email Address</label>
                <input id="email" type="text" class="input">
              </div>
              <div class="inputfield">
                <label>Phone Number</label>
                <input id="phone" type="text" class="input">
              </div>
              <p id="text13" style="text-align:center;">....</p>
              
              <div class="inputfield">
                <input type="submit" onclick="check()"  value="Submit" class="btn">
              </div>
            </div>
          </div>`
        document.getElementById("saqla").innerHTML = `<p id="company_name">Courier:  "${name}"</p>
                                                                                                                <div id="company_price">Rate:  ${price} $</div>
                                                                                                                `





}


function send_data_all() {
        name = document.getElementById('name').value

        phone = document.getElementById('phone').value
        email = document.getElementById('email').value

        country = document.getElementById(`country_id1`).value

        length = document.getElementById(`length`).value
        width = document.getElementById(`width`).value
        height = document.getElementById(`height`).value

        company_name = document.getElementById("company_name").innerHTML
        company_price = document.getElementById("company_price").innerHTML
        var url = `saqlash/`
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken,
            },
            body: JSON.stringify({
                'name': name,

                'phone': phone,
                'email': email,

                'country': country,
                'length': length,
                'width': width,
                'height': height,
                'weight': natija,
                'company_name': company_name,
                'company_price': company_price,
            })
        })
            .then((response) => {
                response.json().then((data) => {
                    data = data['data']
                })
            })

        document.getElementById('saqla2').innerHTML = `
            <p>Name:      ${name}</p>
            <p>phone:     ${phone}</p>
            <p>email:     ${email}</p>
            <p>weight:    ${weight} kg</p>
            <p>country:   ${country}<p>
            <p>${company_name}</p>
            <p>${company_price}</p>
            `
    }

    function check() {

                                                            name = document.getElementById('name').value
                                                            phone = document.getElementById('phone').value
                                                            if (name != ""  && phone != "") {
                                                                send_data_all()
                                                                document.getElementById("please").innerHTML = `Ma'lumotlar:`
                                                                document.getElementById("4div").hidden = !document.getElementById("4div").hidden;


                                                            } else {
                                                                document.getElementById("text13").innerHTML = `<p style="color:red"><b>please try again!!!</b></p> `
                                                            }
                                                        }
