import raylibpy as rl
import ballslogic as l
import time
rl.init_window(600, 300, "Cricket")

font_size = 70
clicked = False
balls = 12
score = []
offscreen = l.choose(5)
onscreen = ["0" for x in range(len(offscreen))]
onscreen_images = rl.load_image("cric-image.png")
onscreen_text = rl.load_texture_from_image(onscreen_images)
number_color = rl.BLACK
background_color = rl.LIGHTGRAY

def getScore(score,balls):
    runs = 0
    wickets = 0
    for x in range(len(score)):
        match score[x]:
            case "wicket":
                wickets+=1
            case "no ball":
                r = l.choose(1,nob=True)[0]
                # score[x] += ("("+str(r)+")")
                runs+=r
            case "wide":
                runs+=1
            case default:
                runs+=score[x]
    return (runs , wickets)

while not rl.window_should_close():
    rl.set_target_fps(60)
    # rl.draw_fps(0,0)
    for i in range(len(offscreen)):
        mouse_pos = rl.get_mouse_position()
        number_pos = rl.Vector2(100 * (i + 1), 150)
        if(not clicked and balls != 0):
            if rl.check_collision_point_rec(mouse_pos, rl.Rectangle(int(number_pos.x - onscreen_text.width / 2), int(number_pos.y - onscreen_text.height / 2),
                                                                    onscreen_text.width,
                                                                    onscreen_text.height)):
                if rl.is_mouse_button_pressed(rl.MOUSE_LEFT_BUTTON):
                    clicked = True
                    print(offscreen[i])
                    score.append(offscreen[i])
                    balls-=1
                    offscreen = l.choose(len(offscreen))
                    clicked = False

    rl.begin_drawing()
    rl.clear_background(background_color)
    for i in range(len(onscreen)):
        number_pos = rl.Vector2(100 * (i + 1), 150)

        rl.draw_texture(onscreen_text, int(number_pos.x - onscreen_text.width / 2), int(number_pos.y - onscreen_text.height / 2), rl.WHITE)
    runs , wickets = getScore(score , balls)
    rl.draw_text("SCORE : "+str(runs)+"/"+ str(wickets)+":", 0,
                 0,
                 font_size // 4,
                 number_color)
    rl.draw_text ("scoreboard : "+str(score), 0,
                 50,
                 font_size // 4,
                 number_color)
    rl.draw_text("over : "+str((12-balls)//6)+"."+str((12-balls)%6), 0,
                 30,
                 font_size // 4,
                 number_color)

    rl.end_drawing()

rl.close_window()