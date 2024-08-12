local trigger1 = script.Parent.Trigger1
local trigger2 = script.Parent.Trigger2
local monster = script.Parent.Monster
local targetPosition = Vector3.new(84.26, 2.82, 165.35)
local moveTime = 10 
local function moveToTarget(part, targetPosition, moveTime)
	local startTime = tick() -- Получаем текущее время
	local startPosition = monster.Position -- Начальная позиция
	-- Главный цикл, который будет выполняться до завершения перемещения
	while tick() - startTime < moveTime do
		local elapsed = tick() - startTime -- Прошедшее время
		local alpha = math.clamp(elapsed / moveTime, 0, 1) -- Интерполяционный коэффициент

		-- Вычисляем новую позицию с помощью интерполяции
		local newPosition = startPosition:Lerp(targetPosition, alpha)

		-- Обновляем позицию объекта
		monster.Position = newPosition

		-- Ждем следующего кадра
		wait()
	end

	-- Устанавливаем финальную позицию, чтобы избежать возможных неточностей
	monster.Position = targetPosition
end
local part = script.Parent -- ссылка на Part

-- Функция, которая вызывается при касании Part
local function onTouch(hit)
	local character = hit.Parent
	-- Проверяем, является ли родитель касающегося объекта персонажем
	if character:FindFirstChildOfClass("Humanoid") then
		trigger1:Destroy()
		moveToTarget(trigger2, targetPosition, moveTime)
		-- Здесь вы можете добавить любые действия, которые хотите выполнить
	
	end
end

-- Подключаем функцию к событию Touched
trigger1.Touched:Connect(onTouch)
