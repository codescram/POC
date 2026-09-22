const portfolioData = {
    Name:"Raj Kumar",
    Title: "Frontend Developer",
    ImageUrl:"profile-pic.jpg",
    bio:"I am a Frontend & UI Development Expert with proven experience in building scalable Angular-based Single Page Applications (SPAs), optimizing performance, and creating reusable UI components that drive user engagement and business value.",
    links:[
        {name:"Linkedin", url:"https://www.linkedin.com/in/rajdesignden/"},
        {name:"GitHub", url:"https://github.com/codescram"},
    ]

}

function createPortfolio(data){
    //Get Container Element
    const mainContainer = document.getElementById('portfolio-container');

    //Create card block
    const cardElement = document.createElement('div');
    cardElement.classList.add('card');

    //Create and set image
    const imageElement = document.createElement('img')
    imageElement.src = data.ImageUrl;
    imageElement.alt = data.Name;
    imageElement.classList.add('profilepic');

    //Create Name Element
    const nameElement = document.createElement('h2')
    nameElement.textContent = data.Name;
    nameElement.classList.add('name');

    //Create Title Element
    const titleElement =  document.createElement('h3')
    titleElement.textContent = data.Title;
    titleElement.classList.add('title');

    //create bio element
    const bioElement = document.createElement('p');
    bioElement.textContent = data.bio;
    bioElement.classList.add('bio');

    //create link container
    const linkContainer = document.createElement('ul');
    linkContainer.classList.add('links');

    // create links element throu loop
    data.links.forEach(element => {
        const link = document.createElement('li');
        const anchor = document.createElement('a')
        anchor.textContent=element.name;
        anchor.href = element.url;
        anchor.target = "_blank"
        link.appendChild(anchor)
        link.classList.add('link');
        linkContainer.appendChild(link);
    });

    //Insert All in main-conatiner
    cardElement.appendChild(imageElement);
    cardElement.appendChild(nameElement);
    cardElement.appendChild(titleElement);
    cardElement.appendChild(bioElement);
    cardElement.appendChild(linkContainer);
    mainContainer.appendChild(cardElement);

}

createPortfolio(portfolioData)