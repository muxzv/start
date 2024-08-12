-- Получение ссылок на объекты
local door = script.Parent:FindFirstChild("Door")
local buttonFolder = script.Parent:FindFirstChild("ButtonFolder")
local button2 = buttonFolder and buttonFolder:FindFirstChild("Button2")

-- Переменная для отслеживания количества нажатий
local gen = 0

-- Функция для обработки нажатия кнопки
local function onButtonPressed(buttonPrompt, button)
	-- Увеличиваем значение переменной gen
	gen = gen + 1

	-- Меняем цвет нажатой кнопки на зелёный
	button.BrickColor = BrickColor.new("Bright green")

	-- Удаляем ProximityPrompt
	buttonPrompt:Destroy()

	-- Проверяем, если gen равно 2
	if gen == 1 then
		-- Удаляем дверь
		if door then
			door:Destroy()
		end
	end
end

if button2 and button2:FindFirstChild("ProximityPrompt") then
	button2.ProximityPrompt.Triggered:Connect(function()
		onButtonPressed(button2.ProximityPrompt, button2)
	end)
end
