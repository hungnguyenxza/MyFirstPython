
// Khai báo function
// function sayHello() {
//     console.log("Hello world");
//     console.log("Xin chào các bạn");
// }

// Gọi function
//sayHello();
//sayHello();

// function tinhTong(a, b){
//     let sum = a + b;
//     console.log("Gia tri cua a: " + a);
//     console.log("Gia tri cua b: " + b);
//     console.log("Tong cua 2 so la: " + sum);
// }

// let x = 10;
// let y = 20;
// tinhTong(y, x);

// //Khai báo function
// function tinhTong3So(x, y, z){
//     let sum = x + y + z;
//     console.log("Tong cua 3 so la: " + sum);
// }

// //sử dụng function
// let x = 10, y = 20, z = 30;
// tinhTong3So(x, y, z);

// function welcome(name){
//     console.log("Xin chào: " + name);
// }

// let ten = prompt("Nhập tên: ");
// welcome(ten);

// function giaiPTBac2(a, b, c){
//     //Code giải PT
//     let delta = b * b - 4 * a * c;

//     if(delta > 0){
//         let x1 = (-b + Math.sqrt(delta)) / (2 * a);
//         let x2 = (-b - Math.sqrt(delta)) / (2 * a);
//         console.log("Phương trình có 2 nghiệm:");
//         console.log("x1 = " + x1);
//         console.log("x2 = " + x2);
//     }
//     else if (delta == 0){
//         let x = -b / (2 * a);
//         console.log("Phương trình có nghiệm duy nhất: ");
//         console.log("x = " + x);
//     }
//     else {
//         console.log("Phương trình vô nghiệm");
//     }
// }

// let a = Number(prompt("Nhập a: "));
// let b = Number(prompt("Nhập b: "));
// let c = Number(prompt("Nhập c: "));
// giaiPTBac2(a, b, c);

// function tinhTong(a, b){
//     let sum = a + b;
//     return sum;
// }

// let x = 12;
// let y = 20;
// let tong = tinhTong(x, y);
// console.log("Tổng là: " + tong);

// Nhập vào 1 số, trả về ước số lớn nhất:

// function ULN(n){
//     let array = [];
//     for (let index = n-1; index > 0; index--) {
//         if(n % index == 0){
//             array.push(index);
//         }
//     }
//     return array;
// }

// let uocLonNhat = ULN(204);
// console.log(uocLonNhat);



