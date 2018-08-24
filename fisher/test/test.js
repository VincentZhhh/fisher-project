// function aa(a){
//     console.log(a)
// };
// var b = 'c';
//
// function bb(b, callback){
//     b = b;
//     var c = b+'d'
//     callback(c,b)
//     callback(b,c)
// }
//
// bb('cc',function (x,y) {
//     console.log(x,y)
// })
//
// console.log('last:'+b)
// ------------------------------------------------------------------------------------

// function out(res, callback){
//     // res = res + 'callback'
//     callback(res.constructor)
//
// }
// class TS{
//     constructor(name, age, sex, school){
//         this.name = name
//         this.age = age
//         this.sex = sex
//         this.school = school
//     }
//
//     cons(){
//         console.log(this.name, this.age, this.sex, this.school)
//     }
//
//     conss(re){
//         out(this.name, function(resu){console.log(resu+re)})
//         out(re, function(resu){console.log(resu)})
//     }
// }
//
// t = new TS('zws', 21, 'male', 'bnuz')
// t.conss('hello')
// exports.t = t
// if(!module.parent) {
//     console.log(module)
//     console.log('-----------------------------------')
// }
// -------------------------------------------------------------------------------------
// a = 1
// function t(a){a = 2}
// t(a)
// var a
// console.log(a)

var citydict = {}

var data = {a:[{name:'北京', code:'bjx'},{name:'北京', code:'bjx'},{name:'深圳', code:'szx'}],
    b:[{name:'北京京', code:'bjxx'},{name:'北京', code:'bjx'},{name:'深圳圳', code:'szzx'}],}

// console.log(data)
exports.fun = function convert2chinese(code) {
    if(Object.keys(citydict).length > 0){
        console.log('dict done')
        return(citydict[code])
    }
    // console.log(Object.keys(citydict))
    else{
        for (data_index in data) {
            // console.log(data_index)
            for (city_index of data[data_index]) {
                // console.log(city_index)
                if (!citydict.hasOwnProperty(city_index.code)) {
                    citydict[city_index.code] = city_index.name
                }
                else {
                    continue
                }
            }
        }
        return(citydict[code])
    }
}
// console.log(convert2chinese('bjx'))
// console.log(citydict)

// exports.fun = convert(city){
//     ret
// }