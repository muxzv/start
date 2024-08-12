local TweenService = game:GetService("TweenService")
local door = script.Parent -- Дверь, к которой прикреплен скрипт

-- Конфигурация анимации
local doorOpenPosition = door.Position + Vector3.new(5, 0, 0) -- Позиция двери при открытии (например, на 5 единиц вправо)
local tweenInfo = TweenInfo.new(2, Enum.EasingStyle.Linear, Enum.EasingDirection.InOut) -- Продолжительность 2 секунды

-- Цель твина
local tweenGoal = {Position = doorOpenPosition}
local tween = TweenService:Create(door, tweenInfo, tweenGoal)

-- Функция открытия двери
local function onDoorClick()
	tween:Play() -- Запускаем анимацию
	script.Parent.ClickDetector:Destroy()
end

-- Убедитесь, что дверь может быть активирована (например, добавьте возможность взаимодействия с объектом)
door.ClickDetector.MouseClick:Connect(onDoorClick)
