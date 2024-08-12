-- Получаем ссылку на модель, содержащую объект
local model = script.Parent

-- Ищем первый объект типа Part в модели
local part = model.BasePart

-- Проверяем, найден ли объект
if not part then
	warn("Part not found in the model")
	return
end

-- Задаем список позиций для перемещения
local positions = {
	CFrame.new(-86.04, 4.47, 110.27),
	CFrame.new(-86.75, 5.31, 100.09),
	CFrame.new(-84.12, 11.35, 87.76),
	CFrame.new(-82.47, 8.12, 77.22)
}

-- Задаем интервал перемещения в секундах
local moveInterval = 5

-- Переменная для отслеживания текущей позиции
local currentIndex = 1

-- Функция для перемещения объекта на следующую позицию
local function movePart()
	-- Обновляем CFrame объекта на следующую позицию
	part.CFrame = positions[currentIndex]

	-- Обновляем индекс позиции для следующего перемещения
	currentIndex = (currentIndex % #positions) + 1
end

-- Запускаем перемещение объекта каждые 5 секунд
while true do
	movePart()
	wait(moveInterval)
end
