package sample;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.LinearGradient;
import javafx.scene.paint.Paint;
import java.util.ArrayList;
import java.util.Arrays;

public class Level
{
    private final Grid levelGrid;
    private ArrayList<Entity> objects;
    private ArrayList<Entity> originalObjects;
    private ArrayList<Entity> deadObjects = new ArrayList<>();
    private Paint originalColor;
    private Paint completedColor;
    private boolean completed;

    public Level(int size, Paint gridColor)
    {
        levelGrid = new Grid(size, gridColor);
        objects = new ArrayList<>();
        originalObjects = new ArrayList<>();
        originalColor = gridColor;

    }

    public Level(int size, Paint gridColor, Entity... entities)
    {
        levelGrid = new Grid(size, gridColor);
        objects = new ArrayList<>();
        originalObjects = new ArrayList<>();
        originalColor = gridColor;
        originalPopulate(entities);
        populate(entities);
    }

    public Level(int size, Paint gridColor, Paint completedColor, Entity... entities)
    {
        levelGrid = new Grid(size, gridColor);
        objects = new ArrayList<>();
        originalObjects = new ArrayList<>();
        originalColor = gridColor;
        this.completedColor = completedColor;
        originalPopulate(entities);
        populate(entities);
    }

    public Level(int size, Paint gridColor, Paint completedColor)
    {
        levelGrid = new Grid(size, gridColor);
        objects = new ArrayList<>();
        originalObjects = new ArrayList<>();
        originalColor = gridColor;
        this.completedColor = completedColor;
    }

    public void populate(Entity... entities)
    {
        objects.addAll(Arrays.asList(entities));
        defaultControllable();
    }

    public void originalPopulate(Entity... entities)
    {
        for(Entity e : entities)
        {
            originalObjects.add(e.copy());
        }
    }

    public void reset()
    {
        objects = new ArrayList<>();
        for(Entity e : originalObjects)
        {
            objects.add(e.copy());
        }
        defaultControllable();
    }

    public void display(GraphicsContext surface)
    {
        //grid
        levelGrid.minimalDraw(surface);
        //entities
        for(Entity entity : objects)
        {
            entity.drawInGrid(levelGrid, surface);
        }
    }

    public Entity findControllable()
    {
        for(Entity block : objects)
        {
            if(block.isControllable() && block.getPlayable())
            {
                return(block);
            }
        }
        //No selected objects? Get a default one.
        return(defaultControllable());
    }

    public boolean atLeastOnePlayable()
    {
        for(Entity block : objects)
        {
            if(block.getPlayable())
            {
                return(true);
            }
        }
        return(false);
    }

    public Entity defaultControllable()
    {
        for(Entity block : objects)
        {
            if(block.getPlayable())
            {
                block.setControllable(true);
                return(block);
            }
        }
        //THIS SHOULD NEVER RUN
        //System.out.println("Error: Could not find any playable objects.");
        return(objects.get(0));
    }

    public void enforceInput(String code)
    {
        //check at least one playable
        if(!(atLeastOnePlayable()))
        {
            return;
        }

        Entity controllableBox = findControllable();

        //check for webs
        for(Entity e : objects)
        {
            if(e.getX() == controllableBox.getX() && e.getY() == controllableBox.getY() && e.getType().equals("Web"))
            {
                return;
            }
        }

        controllableBox.gridKeyMovement(code);

        controllableBox.enforcePhysics(code, this);

        clearDeadObjects();
    }

    public void setControllable(double mouseX, double mouseY)
    {
        double transformedX;
        double transformedY;
        //boolean atLeastOneControllable = false;
        for(Entity entity : objects)
        {
            if(entity.getPlayable())
            {
                //detect mouse clicking on the thing
                transformedX = levelGrid.getSmallBound() + 85 * entity.getX();
                transformedY = levelGrid.getSmallBound() + 85 * entity.getY();

                //atLeastOneControllable = true;
                entity.setControllable(transformedX <= mouseX && mouseX <= transformedX + 85
                        && transformedY <= mouseY && mouseY <= transformedY + 85);
            }

        }
    }

    public Grid getLevelGrid()
    {
        return levelGrid;
    }

    public ArrayList<Entity> getObjects()
    {
        return objects;
    }

    public void clearDeadObjects()
    {
        for (Entity deadObject : deadObjects) {
            objects.remove(deadObject);
        }

        deadObjects = new ArrayList<>();
    }

    public void addDeadObject(Entity deadEntity)
    {
        deadObjects.add(deadEntity);
    }

    public boolean isCompleted()
    {
        //static colors
        Paint sunset = LinearGradient.valueOf("from 0% 0% to 100% 100%, Red 0%, Gold 100%");
        Paint plasma = LinearGradient.valueOf("from 0% 0% to 100% 100%, Magenta 0%, SlateBlue 100%");
        Paint bloody = LinearGradient.valueOf("from 0% 0% to 100% 100%, Red 0%, Maroon 100%");
        boolean tracker = true;
        for(Entity entity : objects)
        {
            if(("" + entity.getClass()).equals("class sample.Sensor") && !entity.getActivated(this))
            {
                levelGrid.setColor(originalColor);
                tracker = false;
            }
        }

        if(tracker)
        {
            levelGrid.setColor(completedColor);
            //set color of everything to gradient
            for(Entity entity : objects)
            {
                entity.setColor(completedColor);
            }
        }
        completed = tracker;
        return(tracker);

    }

    public boolean getCompleted()
    {
        return completed;
    }

    public Level copy()
    {
        Level copied = new Level(levelGrid.getSize(), levelGrid.getColor(), completedColor);

        for(Entity entity : objects)
        {
            copied.populate(entity);
            copied.originalPopulate(entity);
        }

        return(copied);
    }
}
