package sample;

import javafx.scene.canvas.GraphicsContext;
import javafx.scene.paint.Color;
import javafx.scene.paint.Paint;

import java.util.ArrayList;

public class Slider extends Box
{
    public Slider(double x, double y)
    {
        super(x, y, true, Color.BROWN, "Horizontal");
    }

    public Slider(double x, double y, String type)
    {
        super(x, y, true, Color.BROWN, type);
    }


    @Override
    public void gridKeyMovement(String code)
    {
        if(code.equals("RIGHT") && getType().equals("Horizontal"))
        {
            moveX(1);
        }
        if(code.equals("LEFT") && getType().equals("Horizontal"))
        {
            moveX(-1);
        }
        if(code.equals("UP") && getType().equals("Vertical"))
        {
            moveY(-1);
        }
        if(code.equals("DOWN") && getType().equals("Vertical"))
        {
            moveY(1);
        }
    }

    @Override
    public void drawInGrid(Grid theGrid, GraphicsContext surface)
    {
        //calculate margins (size of slider is 85)
        double margin = (85 - getSize()) / 2.0;
        double centerX = theGrid.getSmallBound() + 85 * getX() + margin + getSize() / 2.0;
        double centerY = theGrid.getSmallBound() + 85 * getY() + margin + getSize() / 2.0;

        Paint previousFill = surface.getFill();
        surface.setFill(getColor());
        //main rectangle
        surface.fillRect(theGrid.getSmallBound() + 85 * getX() + margin, theGrid.getSmallBound() + 85 * getY() + margin, getSize(), getSize());

        //control indicator
        if(isControllable())
        {
            surface.setFill(Color.GOLD);
        }
        else
        {
            surface.setFill(Color.GRAY);
        }

        if(getType().equals("Vertical"))
        {
            double[] xPoints = {centerX, centerX + 7, centerX + 7, centerX, centerX - 7, centerX - 7};
            double[] yPoints = {centerY - 20, centerY - 10, centerY + 10, centerY + 20, centerY + 10, centerY - 10};
            surface.fillPolygon(xPoints, yPoints, 6);
        }
        else
        {
            double[] yPoints = {centerY, centerY + 7.0, centerY + 7.0, centerY, centerY - 7.0, centerY - 7.0};
            double[] xPoints = {centerX - 20, centerX - 10, centerX + 10, centerX + 20, centerX + 10, centerX - 10};
            surface.fillPolygon(xPoints, yPoints, 6);
        }


        //return back to whatever fill we were using before
        surface.setFill(previousFill);
    }

    @Override
    public Slider copy()
    {
        return(new Slider(getX(), getY(), getType()));
    }

}
