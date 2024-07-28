-- Put in StarterPlayerScripts
-- You do not need to change anything unless you want the blur to be more intense (change the 15 to a higher number if desired)

local colorEffect = Instance.new("ColorCorrectionEffect", game.Lighting)
local blurEffect = Instance.new("BlurEffect", game.Lighting)

game.Players.LocalPlayer.CharacterAdded:Connect(function()
	local humanoid = game.Players.LocalPlayer.Character:WaitForChild("Humanoid")
	while humanoid.Health > 0 do
		colorEffect.TintColor = Color3.new(1, humanoid.Health / humanoid.MaxHealth, humanoid.Health / humanoid.MaxHealth)
		blurEffect.Size = 15 * (1 - humanoid.Health / humanoid.MaxHealth)
		wait()
	end
	colorEffect.TintColor = Color3.new(1,0,0)
	blurEffect.Size = 15
end)
