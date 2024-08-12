-- Получаем часть, на которой находится скрипт
local part = script.Parent

-- Получаем объект проксимити промпт
local proximityPrompt = part:FindFirstChildOfClass("ProximityPrompt")

-- Функция, которая будет вызываться при активации проксимити промпта
local function onPromptTriggered(player)
	part.Anchored = false  -- Выводим "1" в консоль
	proximityPrompt:Destroy()
end

-- Привязываем функцию к событию "Triggered" проксимити промпта
if proximityPrompt then
	proximityPrompt.Triggered:Connect(onPromptTriggered)
end
