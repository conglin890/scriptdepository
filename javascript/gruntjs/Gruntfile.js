module.exports = function(grunt) {

  grunt.initConfig({
    
    //代码检查
    jshint: {
      files: ['Gruntfile.js', 'src/**/*.js', 'test/**/*.js'],
      options: {
        globals: {
          jQuery: true,
          curly:true,   //循环或者条件语句必须使用花括号包围
          es3: true,  //兼容低级浏览器 IE 6/7/8/9
          freeze: true,  //禁止重写原生对象的原型，比如 Array ， Date
          indent: true, //代码缩进
          quotmark: false,   //为 true 时，禁止单引号和双引号混用
          undef: true,  //变量未定义
          unused: true, //变量未使用
          maxparams: 4, //最多参数个数
          maxdepth: 4,  //最大嵌套深度
          strict:true,  //严格模式
          lastsemic:true, //检查一行代码最后声明后面的分号是否遗漏
          sub:true, //person['name'] vs. person.name
          devel:true //定义用于调试的全局变量： console ， alert
        }
      }
    },
    watch: {
      files: ['<%= jshint.files %>'],
      tasks: ['jshint']
    }
  });

  grunt.loadNpmTasks('grunt-contrib-jshint');
  //grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['jshint']);

};






