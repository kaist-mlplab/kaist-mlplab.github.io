// 수식을 KaTeX로 "미리" 렌더링해 index.html에 정적 HTML(+MathML)로 박아 넣는 도구.
// 페이지에서 JS를 실행하지 않아도 수식이 보이고, MathML 안에 TeX 원문이 남아 AI/크롤러도 읽을 수 있다.
//
// 사용법
//   1) index.html 본문에 인라인 수식은 [[i:TeX]], 블록 수식은 [[d:TeX]] 로 적는다.
//        예) overlap coefficient [[d:\int \min\big(p^{k}(v), p^{k'}(v)\big)\,dv]]
//   2) npm install katex@0.16.11   (레포 밖 임시 폴더에서 해도 됨)
//   3) node tools/render-math.js index.html
//   4) <head>에 아래 CSS가 있는지 확인:
//      <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
// 마커 뒤에는 공백, '<', '.', ',', ';', ')', '-' 중 하나가 와야 한다.
const fs = require('fs');
const katex = require('katex');
const file = process.argv[2] || 'index.html';
let n = 0;
const html = fs.readFileSync(file, 'utf8').replace(
  /\[\[([id]):([\s\S]*?)\]\](?=[\s<.,;)-]|$)/g,
  (_, mode, tex) => { n++; return katex.renderToString(tex, { displayMode: mode === 'd', output: 'htmlAndMathml', throwOnError: true }); }
);
fs.writeFileSync(file, html);
console.log(`rendered ${n} formulas in ${file}`);
