-- Получаем ссылку на PointLight
local part = script.Parent
local pointLight = part:FindFirstChildOfClass("SpotLight")

-- Если PointLight найден
if pointLight then
	-- Параметры мигания
	local blinkInterval = 0.1 -- интервал мигания в секундах
	local lightOn = true

	while true do
		-- Изменяем состояние света
		lightOn = not lightOn
		pointLight.Enabled = lightOn

		-- Ждем указанное время
		wait(blinkInterval)
	end
else
	warn("PointLight не найден в Part")
end
