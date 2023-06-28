def McEau():

    from mcpi.minecraft import Minecraft
    mc = Minecraft.create()
    x,y,z = mc.player.getPos()
    mc.setBlock(x,y,z,9)
