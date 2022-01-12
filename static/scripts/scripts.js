
void function signupFormFieldAddClass(){

    let form_username = document.getElementById('id_username')
    form_username.placeholder='Username';
    form_username.className += ' form-control';

    let form_email = document.getElementById('id_email')
    form_email.placeholder='Email';
    form_email.className += ' form-control';

    let form_password1 = document.getElementById('id_password1')
    form_password1.placeholder='Password';
    form_password1.className += ' form-control';

    let form_password2 = document.getElementById('id_password2')
    form_password2.placeholder='Confirm Password';
    form_password2.className += ' form-control';


}();

const navSlide = () => {
    const resize = document.querySelector('.resize');
    const nav = document.querySelector('.nav-link');

    resize.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
    });
}

navSlide();