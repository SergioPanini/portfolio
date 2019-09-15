unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls;
 const N = 200;
type

  { TForm1 }
   AryBtn = array[1..N, 1..N] of TButton;

  TForm1 = class(TForm)
    procedure FormCreate(Sender: TObject);
    procedure MV(Sender: TObject);

  private
  public
  end;

var

  Form1: TForm1;
  Btns : AryBtn;

implementation

{$R *.lfm}

{ TForm1 }


//процедура инициализации кнопок
procedure TForm1.FormCreate(Sender: TObject);
var i, x, y : integer;
begin
     i := 1;
     for y :=1 to N do
         for x :=1 to N do
             begin
              Btns[x, y] := TButton.Create(Form1); //создаем кнопки в форме 1
              Btns[x, y].parent:=Form1;  //указываем что рисовать будем на форме 1
              Btns[x, y].Left := x*50;
              Btns[x, y].Top := y* 50;
              Btns[x, y].visible:=true;
              Btns[x, y].Width:=49;
              Btns[x, y].Height:=49;
              Btns[x, y].Enabled := True;
              Btns[x, y].TabStop := True;
              Btns[x, y].ParentFont := True;
              Btns[x, y].OnClick := @MV;
              Btns[x, y].Caption:= concat('_', IntToStr(i)); //'.' + IntToStr(i);
              Btns[x, y].Name := concat('_',IntToStr(x), IntToStr(y)); //имя кнопки содержит индексы массива в котором находится кнопка

              i :=  i + 1;
             end;
     Btns[N, N].Visible:= false;
     //Form1.Show;
     //Btns[4, 4].Name := '_';
end;

//процедура обработки нажатия кнопки
procedure TForm1.MV(Sender: TObject);
var x, y : integer;
  x_o, y_o : integer;
  x_f, y_f : integer;
  i:integer;
procedure Normcords(var x, y:integer);
begin
     if(x > N ) then x := N;
     if(x < 1) then x := 1;
     if(y > N ) then y := N;
     if(y < 1) then y := 1;
end;

function win : boolean;
var i, x, y, z : integer;
begin
    i := 1;
    z := 1;
    win := false;
    for y :=1 to N do
         for x :=1 to N do
             begin
                  if(Btns[x,y].Caption = Concat('_',IntToStr(i))) then z := z + 1;
                  i :=  i + 1;
             end;
    if(z = N * N - 1) then
    begin
       for y :=1 to N do
         for x :=1 to N do
           Btns[x, y].Color := (125);
    end;
end;

begin
    x_f := N + 1;
    y_f := N + 1;


     if (Sender is TButton) then
     begin
       //TButton(Sender).Caption := TButton(Sender).Name;
       //получение индексов массива кнопки которая вызвала процедуру
       x := StrToInt(TButton(Sender).Name[2]);
       y := StrToInt(TButton(Sender).Name[3]);

       //запоминаем старые индексы кнопки для того что бы ее стереть
       x_o := x;
       y_o := y;

       //поиск пустого места не по кроям
       if( (x > 1) and (x < N) and (y > 1) and (y < N) ) then
       begin
            if (Btns[x+1, y].Visible = false) then
               begin x_f := x + 1; y_f := y; end;
            if (Btns[x-1, y].Visible = false) then
               begin x_f := x - 1; y_f := y; end;
            if (Btns[x, y+1].Visible = false) then
               begin x_f := x; y_f := y + 1; end;
            if (Btns[x, y-1].Visible = false) then
               begin x_f := x; y_f := y - 1; end;
       end;

       //поиск пустого места по краям

       x := x_o; y := y_o;
       x := x+1; y := y;
       Normcords(x,y);
       if (Btns[x, y].Visible = false) then
          begin x_f := x; y_f := y; end;

       x := x_o; y := y_o;
       x := x-1; y := y;
       Normcords(x,y);
       if (Btns[x, y].Visible = false) then
          begin x_f := x; y_f := y; end;

       x := x_o; y := y_o;
       x := x; y := y+1;
       Normcords(x,y);
       if (Btns[x, y].Visible = false) then
          begin x_f := x; y_f := y; end;

       x := x_o; y := y_o;
       x := x; y := y-1;
       Normcords(x,y);
       if (Btns[x, y].Visible = false) then
          begin x_f := x; y_f := y; end;


       if ((x_f <> N + 1) and (y_f <> N + 1)) then
       begin
            Btns[x_f, y_f].Visible := true;
            Btns[x_f, y_f].Caption := Btns[x_o, y_o].Caption;
            Btns[x_o, y_o].Visible := false;
            Btns[x_o, y_o].Caption := '_';


            //Btns[x_f, y_f].Visible := true;
            //Btns[x_f, y_f].Caption := 'GGGG';
       end;

    //win();
    end;
    //Btns[StrToInt(TButton(Sender).Name[2]),StrToInt(TButton(Sender).Name[3])].Visible:= false;
end;


end.

