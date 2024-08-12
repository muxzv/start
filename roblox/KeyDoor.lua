script.Parent.Touched:Connect(function(h)
	if h.Parent.Name == "Key" then
		h.Parent:Destroy()
		script.Parent:Destroy()
	end
end)
