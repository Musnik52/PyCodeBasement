function dothis() { // הגדרת פונקציה
  var fn = document.getElementById("fnid").value //הגדרת משתנה שם פרטי
  var ln = document.getElementById("lnid").value // הגדרת משתנה שם משפחה
  if (fn.length == 0 || ln.length == 0) // לולאה
  {
      alert('too short')
      return;
  }
  // הפונקציה מחזירה פקודת HTML של הקלט ואורך המילה
  document.getElementById("result").innerHTML = 
  `${fn.toUpperCase()}<br>${fn.length}<br>${ln.toUpperCase()}<br>${ln.length}`
} // סגירת הפונקציה