import keyboard as k 

k.add_hotkey('ctrl + 1', lambda: k.write("function animate({ duration, draw, timing }) {\n\n    let start = performance.now();\n\n    requestAnimationFrame(function animate(time) {\n        let timeFraction = (time - start) / duration;\n        console.log('time ' + time)\n        console.log('start ' + start)\n        if (timeFraction > 1) timeFraction = 1;\n\n        let progress = timing(timeFraction)\n\n        draw(progress);\n\n        if (timeFraction < 1) {\n            requestAnimationFrame(animate);\n        }\n\n    });\n}", delay = 0.1))

k.wait()


# Как работает
# 1) Устанавливаем pip install keyboard
# 2) Вписываем в функцию k.write() строку которую хотим написать, но перенос строки заменяем на /n . Ето можно сделать здесь - https://codepen.io/jsnelders/pen/qBByqQy
# 3) запускаем скрипт python index.py
# 4) Нажимаем ctrl + 1

# Проблема лайвкодинга при сьемке видео
# 1) Много переписываешь код во время сьемки
# 2) Много ошибаешься во время написания
# 3) При лайвкодинге добаляеться время на исправление ошибок