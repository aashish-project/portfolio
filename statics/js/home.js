
function getreact(element) {
    return element.getBoundingClientRect().top-window.innerHeight
}

var skill_bar=document.getElementsByClassName('skills')[0]
var child_list=skill_bar?skill_bar.querySelectorAll('.bar'):[]
window.addEventListener("scroll",function(){
    if (getreact(skill_bar)>5) {
        for (let index = 0; index < child_list.length; index++) {
                    bar=child_list[index]
                    bar.classList.remove('animate');
                    void bar.offsetWidth;
                    bar.classList.add('animate');
        }
    }
});

var block=document.getElementsByClassName('block')
window.onload=()=>{
    for (let i = 0; i < block.length; i++) {
            block[i].classList.add('fade-in')
    }
}



// var content = document.getElementsByClassName('content')[0];
// window.addEventListener("scroll", () => {
//   if (getreact(content) + 690 <= 0) {
//     var element = document.getElementsByTagName('body')[0];
//     element.style.animation = "color-transition 1.1s linear";
//     setTimeout(() => {
//       element.style.backgroundColor = "black";
//       element.style.color = "white";


//       var heading = document.querySelectorAll('.heading');
//       for (let i = 0; i < heading.length; i++) {
//           heading[i].classList.add('text-green-50');
//         }

//         var subHeading = document.querySelectorAll('.sub-heading');
//         for (let i = 0; i < subHeading.length; i++) {
//             subHeading[i].classList.add('text-green-50');
//         }


//         var link = document.querySelectorAll('.link_a');
//         for (let i = 0; i < link.length; i++) {
//             link[i].classList.add('text-green-100');
//         }
//     }, 1000);
//   }
//   else if (getreact(content)+522<=0){
//     var element = document.getElementsByTagName('body')[0];
//     element.style = "animation:color-transition-backword 2s linear;";
//     console.log(element)
//     console.log(getreact(content))
//     setTimeout(()=>{
//         element.style.backgroundColor = "black";
//         element.style.color = "white";
//     },1900)
//   }
// });
