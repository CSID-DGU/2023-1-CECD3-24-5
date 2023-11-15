const { override, fixBabelImports, addLessLoader } = require('customize-cra');

module.exports = override(
  fixBabelImports('import', {
    libraryName: 'antd',
    libraryDirectory: 'es',
    style: true,
  }),
  addLessLoader({
    lessOptions: {
      math: 'always',
      javascriptEnabled: true,
      modifyVars: { 
        // 'primary-color': '#398D78'
    },
    },
  }),
);
