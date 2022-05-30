# קביעת תשתית - שפת התכנות
# FROM baseImage
FROM node
# הגדרת נתיב בו תתבצע הפעולה
# WORKDIR /the/workdir/path
WORKDIR /app
# הגדרת הקבצים שיועתקו למכולה (מקור ויעד)
# COPY source destination
COPY . ./
# הגדרת פעולה תחילית להרצה
# RUN command
RUN npm install
# מתן הרשאה לצאת מגבולות הבידוד של המכולה
# EXPOSE port
EXPOSE 80
# הרצת פעולה פנימית בתוכן המכולה
# CMD [ "executable" ]
CMD [ "node", "server.js" ]