/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (function() { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./components/main.js":
/*!****************************!*\
  !*** ./components/main.js ***!
  \****************************/
/***/ (function(__unused_webpack_module, __webpack_exports__, __webpack_require__) {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _main_scss__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./main.scss */ \"./components/main.scss\");\n\n\nfunction colorRatings(item, total_rating) {\n  // Update stars coloring in form\n  var selected_rating = item.charAt(item.length - 1);\n\n  for (var i = 0; i < total_rating; i++) {\n    if (i <= Number(selected_rating)) {\n      document.getElementById('id_review-rating_' + i).classList.add('star-full');\n      document.getElementById('id_review-rating_' + i).classList.remove('star-empty');\n    } else {\n      document.getElementById('id_review-rating_' + i).classList.add('star-empty');\n      document.getElementById('id_review-rating_' + i).classList.remove('star-full');\n    }\n  }\n}\n\ndocument.addEventListener('DOMContentLoaded', function () {\n  // Wait for document to be loaded\n  var rating_inputs = document.querySelectorAll('#rating input[name=\"review-rating\"]');\n\n  if (rating_inputs) {\n    var _loop = function _loop(item) {\n      // Event listener for checked item\n      rating_inputs[item].addEventListener('click', function () {\n        if (rating_inputs[item].checked) {\n          colorRatings(rating_inputs[item].id, rating_inputs.length);\n        }\n      }); // Set initial stars\n\n      if (rating_inputs[item].checked) {\n        colorRatings(rating_inputs[item].id, rating_inputs.length);\n      }\n    };\n\n    for (var item = 0; item < rating_inputs.length; item++) {\n      _loop(item);\n    }\n  }\n}, false);//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9jb21wb25lbnRzL21haW4uanMuanMiLCJtYXBwaW5ncyI6Ijs7QUFBQTs7QUFFQTtBQUNBO0FBQ0E7O0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBOztBQUVBO0FBQUE7QUFFQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7O0FBRUE7QUFDQTtBQUNBO0FBWEE7O0FBQ0E7QUFBQTtBQVdBO0FBQ0E7QUFDQSIsInNvdXJjZXMiOlsid2VicGFjazovL2xpdHJldmlldy8uL2NvbXBvbmVudHMvbWFpbi5qcz9lZmZiIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCAnLi9tYWluLnNjc3MnXHJcblxyXG5mdW5jdGlvbiBjb2xvclJhdGluZ3MoaXRlbSwgdG90YWxfcmF0aW5nKSB7XHJcbiAgLy8gVXBkYXRlIHN0YXJzIGNvbG9yaW5nIGluIGZvcm1cclxuICBsZXQgc2VsZWN0ZWRfcmF0aW5nID0gaXRlbS5jaGFyQXQoaXRlbS5sZW5ndGggLSAxKTtcclxuICBmb3IgKGxldCBpID0gMDsgaSA8IHRvdGFsX3JhdGluZzsgaSsrKSB7XHJcbiAgICBpZiAoaSA8PSBOdW1iZXIoc2VsZWN0ZWRfcmF0aW5nKSkge1xyXG4gICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnaWRfcmV2aWV3LXJhdGluZ18nICsgaSkuY2xhc3NMaXN0LmFkZCgnc3Rhci1mdWxsJylcclxuICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2lkX3Jldmlldy1yYXRpbmdfJyArIGkpLmNsYXNzTGlzdC5yZW1vdmUoJ3N0YXItZW1wdHknKVxyXG4gICAgfSBlbHNlIHtcclxuICAgICAgZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQoJ2lkX3Jldmlldy1yYXRpbmdfJyArIGkpLmNsYXNzTGlzdC5hZGQoJ3N0YXItZW1wdHknKVxyXG4gICAgICBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnaWRfcmV2aWV3LXJhdGluZ18nICsgaSkuY2xhc3NMaXN0LnJlbW92ZSgnc3Rhci1mdWxsJylcclxuICAgIH1cclxuICB9XHJcbn1cclxuXHJcbmRvY3VtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ0RPTUNvbnRlbnRMb2FkZWQnLCBmdW5jdGlvbiAoKSB7XHJcbiAgLy8gV2FpdCBmb3IgZG9jdW1lbnQgdG8gYmUgbG9hZGVkXHJcbiAgbGV0IHJhdGluZ19pbnB1dHMgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKFxyXG4gICAgJyNyYXRpbmcgaW5wdXRbbmFtZT1cInJldmlldy1yYXRpbmdcIl0nKTtcclxuICBpZiAocmF0aW5nX2lucHV0cykge1xyXG4gICAgZm9yIChsZXQgaXRlbSA9IDA7IGl0ZW0gPCByYXRpbmdfaW5wdXRzLmxlbmd0aDsgaXRlbSsrKSB7XHJcbiAgICAgIC8vIEV2ZW50IGxpc3RlbmVyIGZvciBjaGVja2VkIGl0ZW1cclxuICAgICAgcmF0aW5nX2lucHV0c1tpdGVtXS5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIGZ1bmN0aW9uICgpIHtcclxuICAgICAgICBpZiAocmF0aW5nX2lucHV0c1tpdGVtXS5jaGVja2VkKSB7XHJcbiAgICAgICAgICBjb2xvclJhdGluZ3MocmF0aW5nX2lucHV0c1tpdGVtXS5pZCwgcmF0aW5nX2lucHV0cy5sZW5ndGgpO1xyXG4gICAgICAgIH1cclxuICAgICAgfSlcclxuICAgICAgLy8gU2V0IGluaXRpYWwgc3RhcnNcclxuICAgICAgaWYgKHJhdGluZ19pbnB1dHNbaXRlbV0uY2hlY2tlZCkge1xyXG4gICAgICAgIGNvbG9yUmF0aW5ncyhyYXRpbmdfaW5wdXRzW2l0ZW1dLmlkLCByYXRpbmdfaW5wdXRzLmxlbmd0aCk7XHJcbiAgICAgIH1cclxuICAgIH1cclxuICB9XHJcbn0sIGZhbHNlKTsiXSwibmFtZXMiOltdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./components/main.js\n");

/***/ }),

/***/ "./components/main.scss":
/*!******************************!*\
  !*** ./components/main.scss ***!
  \******************************/
/***/ (function() {

throw new Error("Module build failed (from ./node_modules/mini-css-extract-plugin/dist/loader.js):\nHookWebpackError: Module build failed (from ./node_modules/sass-loader/dist/cjs.js):\nSassError: expected \"{\".\n    ╷\n186 │   h3\r\n    │     ^\n    ╵\n  components\\main.scss 186:5  root stylesheet\n    at tryRunOrWebpackError (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\webpack\\lib\\HookWebpackError.js:88:9)\n    at __webpack_require_module__ (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\webpack\\lib\\Compilation.js:5055:12)\n    at __webpack_require__ (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\webpack\\lib\\Compilation.js:5012:18)\n    at C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\webpack\\lib\\Compilation.js:5083:20\n    at symbolIterator (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\neo-async\\async.js:3485:9)\n    at done (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\neo-async\\async.js:3527:9)\n    at Hook.eval [as callAsync] (eval at create (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\tapable\\lib\\HookCodeFactory.js:33:10), <anonymous>:15:1)\n    at Hook.CALL_ASYNC_DELEGATE [as _callAsync] (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\tapable\\lib\\Hook.js:18:14)\n    at C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\webpack\\lib\\Compilation.js:4990:43\n    at symbolIterator (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\neo-async\\async.js:3482:9)\n-- inner error --\nError: Module build failed (from ./node_modules/sass-loader/dist/cjs.js):\nSassError: expected \"{\".\n    ╷\n186 │   h3\r\n    │     ^\n    ╵\n  components\\main.scss 186:5  root stylesheet\n    at Object.<anonymous> (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\css-loader\\dist\\cjs.js??ruleSet[1].rules[2].use[1]!C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\postcss-loader\\dist\\cjs.js??ruleSet[1].rules[2].use[2]!C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\sass-loader\\dist\\cjs.js??ruleSet[1].rules[2].use[3]!C:\\Users\\hypoc\\PycharmProjects\\p9__\\components\\main.scss:1:7)\n    at C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\webpack\\lib\\javascript\\JavascriptModulesPlugin.js:441:11\n    at Hook.eval [as call] (eval at create (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\tapable\\lib\\HookCodeFactory.js:19:10), <anonymous>:7:1)\n    at Hook.CALL_DELEGATE [as _call] (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\tapable\\lib\\Hook.js:14:14)\n    at C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\webpack\\lib\\Compilation.js:5057:39\n    at tryRunOrWebpackError (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\webpack\\lib\\HookWebpackError.js:83:7)\n    at __webpack_require_module__ (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\webpack\\lib\\Compilation.js:5055:12)\n    at __webpack_require__ (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\webpack\\lib\\Compilation.js:5012:18)\n    at C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\webpack\\lib\\Compilation.js:5083:20\n    at symbolIterator (C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\neo-async\\async.js:3485:9)\n\nGenerated code for C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\css-loader\\dist\\cjs.js??ruleSet[1].rules[2].use[1]!C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\postcss-loader\\dist\\cjs.js??ruleSet[1].rules[2].use[2]!C:\\Users\\hypoc\\PycharmProjects\\p9__\\node_modules\\sass-loader\\dist\\cjs.js??ruleSet[1].rules[2].use[3]!C:\\Users\\hypoc\\PycharmProjects\\p9__\\components\\main.scss\n1 | throw new Error(\"Module build failed (from ./node_modules/sass-loader/dist/cjs.js):\\nSassError: expected \\\"{\\\".\\n    ╷\\n186 │   h3\\r\\n    │     ^\\n    ╵\\n  components\\\\main.scss 186:5  root stylesheet\");");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	!function() {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = function(exports) {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	}();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval-source-map devtool is used.
/******/ 	var __webpack_exports__ = __webpack_require__("./components/main.js");
/******/ 	
/******/ })()
;