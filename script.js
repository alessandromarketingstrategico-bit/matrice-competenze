const grid=document.getElementById('grid');
const colors=[(138, 52, 40), (198, 24, 24), (223, 120, 120), (255, 192, 1), (252, 238, 132), (205, 53, 53), (228, 141, 141), (255, 203, 44), (252, 240, 151), (252, 240, 153), (224, 124, 124), (255, 198, 26), (252, 239, 144), (252, 239, 145), (169, 234, 146), (255, 198, 27), (252, 239, 144), (252, 239, 143), (169, 234, 145), (89, 179, 56), (252, 240, 151), (252, 241, 155), (177, 236, 156), (98, 183, 67), (70, 129, 49)];

function build(){
  for(let i=0;i<25;i++){
    let d=document.createElement('div');
    d.className='cell';
    d.id='c'+(i+1);
    d.style.background='rgb('+colors[i].join(',')+')';
    d.textContent=i+1;
    grid.appendChild(d);
  }
}
function update(){
  let x=parseInt(document.getElementById('x').value);
  let y=parseInt(document.getElementById('y').value);
  for(let i=1;i<=25;i++) document.getElementById('c'+i).classList.remove('highlight');
  let idx=(y-1)*5+x;
  document.getElementById('c'+idx).classList.add('highlight');
}
build();
update();