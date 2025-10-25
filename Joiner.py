'''
who put lua code in a python file

local args = {
    [1] = game:GetService("ReplicatedStorage"):WaitForChild("Lobbies"):WaitForChild("Join")
}

game:GetService("ReplicatedStorage"):WaitForChild("JoiningLobby"):InvokeServer(unpack(args))
'''