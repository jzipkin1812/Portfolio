package sample;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Paint;

import java.util.ArrayList;
import java.util.Arrays;

public class World
{
    private ArrayList<Level> levels;
    private Level undoState;
    private int size;
    private int currentLevel;
    private Paint color;

    public World(Paint color, Level... multipleLevels)
    {
        levels = new ArrayList<>();
        this.color = color;
        populate(multipleLevels);
        currentLevel = 0;


    }

    public void populate(Level... multipleLevels)
    {
        levels.addAll(Arrays.asList(multipleLevels));
        size = levels.size();
    }

    public void display(GraphicsContext surface)
    {
        surface.setFill(color);
        surface.fillRect(0, 0, 800, 800);
        levels.get(currentLevel).display(surface);
    }

    public int getSize()
    {
        return(size);
    }

    public Paint getColor()
    {
        return color;
    }

    public Level getCurrentLevel()
    {
        return(levels.get(currentLevel));
    }

    public int getNumber()
    {
        return(currentLevel);
    }

    public void ascend()
    {
        currentLevel = Math.min(size - 1, currentLevel + 1);
    }

    public void setAs(World other)
    {
        levels = other.levels;
        size = other.size;
        currentLevel = other.currentLevel;
        color = other.color;
    }

    public Level getUndoState()
    {
        return undoState;
    }
    public void setUndoState(Level lvl)
    {
        undoState = lvl;
    }

    public void undo()
    {
        levels.set(currentLevel, undoState.copy());
    }

}
