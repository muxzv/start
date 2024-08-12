local tool = script.Parent --Variable for the tool
local click = tool.ClickDetector --Variable for the clickdetector

click.MouseClick:Connect(function(player) --When the player clicks on the clickdetector
	tool.Parent = player.Backpack --Put the tool into the inventory (Backpack)
end)
